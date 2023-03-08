from locust import HttpUser,SequentialTaskSet,task,constant,events
from locust.exception import StopUser
from config import read_config
# import locust.stats
# locust.stats.CSV_STATS_INTERVAL_SEC = 1 # default is 1 second
# locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 20 
# locust.stats.CONSOLE_STATS_INTERVAL_SEC=25

test_id,num_user=read_config()
url = "sys_perf_check/"+test_id+"/"+num_user
class PerfCheck(SequentialTaskSet):

    @task
    def perf_check(self):
        print(url)
        with self.client.get(url,name="perf_check",catch_response=True) as response:
            print("perf_check:",response.text)

    # @task
    # def on_stop(self):
    #     raise StopUser()


class MySeqTest(HttpUser):
    # fixed_count=1
    wait_time=constant(1)
    host ="https://safev2.cse.iitb.ac.in/"
    # host ="http://127.0.0.1:8000/"
    tasks = [PerfCheck]