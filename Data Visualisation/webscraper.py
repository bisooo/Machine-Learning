import sys, time, csv, requests
from bs4 import BeautifulSoup as soup


def setup(page):
    base_url = 'https://www.psp.cz/sqw/hlasy.sqw?g='
    endpage = 74002
    if( page > endpage ):
        return None
    url = base_url + str(page)
    connection = requests.get(url)
    htmlpage = connection.content.decode('cp1250')
    connection.close()
    return htmlpage

def scrape( htmlpage , write ):
    czech_english = {
        # MONTHS
        'ledna' : '1',
        'února' : '2',
        'března' : '3',
        'dubna' : '4',
        'května' : '5',
        'června' : '6',
        'července' : '7',
        'srpna' : '8',
        'září' : '9',
        'října' : '10',
        'listopadu' : '11',
        'prosince' : '12',
        # DECISIONS
        'NÁVRH BYL PŘIJAT' : 'ACCEPTED',
        'NÁVRH BYL ZAMÍTNUT' : 'REJECTED'
    }

    parser = soup(htmlpage, "html.parser")
    # MEETING INFO - (NO.) MEETING, (NO.) VOTE, (DAY) (MONTH) (YEAR), (TIME)(MEETING NAME)
    meeting_info = parser.h1.text
    meeting_details = meeting_info.split(',')
    meeting_no = meeting_details[0].strip().split('.')[0]
    vote_no = meeting_details[1].strip().split('.')[0]
    meeting_date = meeting_details[2].strip()
    meeting_day = meeting_date.split('.')[0]
    meeting_month = meeting_date.split('.')[1].split('\xa0')[1]
    meeting_month = czech_english.get(meeting_month, meeting_month)
    meeting_year = meeting_date.split('.')[1].split('\xa0')[2]
    meeting_name = meeting_details[3][6:]

    # MEETING DECISION
    meeting_summary = parser.findAll("div", class_="summary")[0]
    meeting_decision = meeting_summary.h2.span.text
    meeting_decision = czech_english.get(meeting_decision, meeting_decision)


    # PRESENT VOTES / MINIMUM REQUIRED VOTES RATIO
    meeting_voting_presence = meeting_summary.p
    present_votes = meeting_voting_presence.findAll("strong")[0].text
    min_votes = meeting_voting_presence.findAll("strong")[1].text

    # TOTAL VOTE RATIOS
    flag = 0
    try:
        meeting_voter_ratio = parser.findAll("tr", bgcolor="#ccffcc")[0]
    except:
        flag = 1
    if( flag ):
        try:
            meeting_voter_ratio = parser.findAll("tr", bgcolor="#ffcccc")[0]
        except:
            flag = -1
        if( flag == - 1 ):
            return
    total_deputies = meeting_voter_ratio.findAll("td")[1].text
    total_yes = meeting_voter_ratio.findAll("td")[2].text
    total_no = meeting_voter_ratio.findAll("td")[3].text
    total_na = meeting_voter_ratio.findAll("td")[4].text
    total_stayed = meeting_voter_ratio.findAll("td")[5].text
    total_sorry = meeting_voter_ratio.findAll("td")[6].text

    # print('\n= MEETING NAME = ' + meeting_name )
    # print('\n= MEETING DAY = ' + meeting_day )
    # print('\n= MEETING MONTH = ' + meeting_month )
    # print('\n= MEETING YEAR = ' + meeting_year )
    print('\n= MEETING NO = ' + meeting_no )
    print('\n= VOTE NO = ' + vote_no )
    # print('\n= MEETING DECISION = ' + meeting_decision )
    # print('\n= PRESENT VOTES = ' + present_votes )
    # print('\n= MIN NO. VOTES = ' + min_votes )
    # print('\n= MEETING VOTER RATIO =')
    # print('TOTAL DEPUTIES = ' + total_deputies )
    # print('TOTAL YES = ' + total_yes )
    # print('TOTAL NO = ' + total_no )
    # print('TOTAL NOT AVAILABLE = ' + total_na )
    # print('TOTAL STAYED = ' + total_stayed )
    # print('TOTAL SORRY = ' + total_sorry )

    vote_dictionary = {
        'A' : 'YES',
        'N' : 'NO',
        '0' : 'N/A',
        'Z' : 'N/A',
        'M' : 'SORRY'
    }

    # PARLIAMENTARY CLUB NAMES ( 1 - 9 ) & SUMMARY OF VOTES
    i = -1
    for parliamentary in parser.findAll("h2", class_="section-title center")[1:10]:
        i += 1
        party = parliamentary.text
        party_name = party.split('(')[0]
        # print(f'\n===== {parl_name}=====')
        for deputy in parser.findAll("ul", class_="results")[i]:
            deputy_name = deputy.a.text
            deputy_vote = deputy.span.text
            deputy_vote = vote_dictionary.get(deputy_vote,deputy_vote)
            # print(f'= {deputy_name} = {deputy_vote}')
            write.writerow([ f'{meeting_no}',f'{vote_no}',f'{meeting_day}',f'{meeting_month}',f'{meeting_year}',f'{party_name}',f'{deputy_name}',f'{deputy_vote}',f'{present_votes}',f'{min_votes}',f'{meeting_decision}'])


def webscraper():
    currentpage = 67018
    file = open('ye.csv', 'w', newline="", encoding="cp1250")
    write = csv.writer(file)
    write.writerow(['meeting#','vote#','day','month','year','party_name','deputy_name','vote','present_votes','min_votes','decision'])
    while True:
        if( currentpage == 67512 or currentpage == 68547 ):
            currentpage += 1
        time.sleep(0.3)
        htmlpage = setup(currentpage)
        if( not htmlpage ):
            return
        scrape(htmlpage, write)
        currentpage += 1

if __name__ == "__main__":
    webscraper()
    sys.exit()
