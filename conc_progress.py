from concordance import conc2csv
import time
from tqdm import tqdm
from threading import Thread
from time import perf_counter
import multiprocessing


words = open("/home/atagun/Masaüstü/VsCode/conc/demofile2.txt", 'r').read().splitlines()

def conc_progress(conc_list, start_idx, end_idx):
    for i in tqdm(conc_list[start_idx:end_idx]):
        time.sleep(0.1)
        conc2csv("/home/atagun/Masaüstü/VsCode/conc/plot.txt", i, 4)

start_time = perf_counter()
# create two new threads
t1 = multiprocessing.Process(target=conc_progress, args=(words, 0, 472))
t2 = multiprocessing.Process(target=conc_progress, args=(words, 472, 944))

# start the threads
t1.start()
t2.start()
# wait for the threads to complete
t1.join()
t2.join()

end_time = perf_counter()

minutes = (end_time - start_time)/60

print(f'It took {minutes: 0.2f} minute(s) to complete.')