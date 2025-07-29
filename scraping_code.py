import requests
from bs4 import BeautifulSoup
url = "https://service.ariba.com/Sourcing.aw/109578004/aw?awh=r&awssk=P4VEdQnG&dard=1&ancdc=1#b0"
response = requests.get(url)

if response.status_code == 200:
    print("request was successful")
    
    # page_content = response.content
    
    # soup = BeautifulSoup(page_content, "html.parser")
    # print(soup.prettify())
    
# #     job_title = soup.find_all("h2", class_="title")
# #     for title in job_title:
# #         print("Job Title", title.text.strip())
# #     else:
# #          print(f"Failed to retrieve content, status code: {response.status_code}")

# # import requests
# # url = 'http://www.google.com/'
# # r = requests.get(url)
# # print(r.status_code)
# # print(r.text)    

# # from requests_futures import sessions

# # sessions = sessions.FuturesSession()

# # futures = [
# #     sessions.get('http://www.google.com/')
# #     for i in range(8)
# # ]

# # results = [
# #     f.result().status_code
# #     for f in futures
# # ]

# # print(results)

# async def one_site(session, url):
#     async with session.get(url) as response:
#         return await response.text()
    
# async def all_sites(sites):
#     async with aiohttp.ClientSession() as session:
#         task = []
#         for url in sites:
#             task = asyncio.ensure_future(one_site(session, url))
#             tasks.append(task)
            
#         finished, unfinished = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
#         res = ''
#         for i in finished:
#             res = i.result()
#         while unfinished:
#             print(f"Canceling {len(unfinished)} remaining tasks")
#             for task in unfinished:
#                 print("Canceling {task}: {task_cancel}".format(task=task, task_cancel=task.cancel()))
                
                

# url_final = 'http://www.google.com/'
# sites = [
#     url_final
# ] * 3
# start_time = time.time()
# rr = asyncio.get_event_loop().run_untill_complete(all_sites(sites))
# duration = time.time() - start_time
    
    
