import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = datetime.datetime.now()
for file in filenames:
    read_info(file)
end = datetime.datetime.now()
print(f'{end - start} (линейный)')

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'{end - start} (многопроцессорный)')





# import multiprocessing
# import time
# import threading
#
#
# counter = 0
#
# def first_worker(n):
#     global counter
#     for i in range(n):
#         counter += 1
#         time.sleep(1)
#     print('The first worker changed a value', counter)
#
#
# def second_worker(n):
#     global counter
#     for i in range(n):
#         counter += 1
#         time.sleep(1)
#     print('The second worker changed a value', counter)
#
#
# # thread1 = threading.Thread(target=first_worker, args=(10,))
# # thread2 = threading.Thread(target=second_worker, args=(5,))
# # thread1.start()
# # thread2.start()
#
# if __name__ == '__main__':
#
#     process1 = multiprocessing.Process(target=first_worker, args=(10, ))
#     process2 = multiprocessing.Process(target=second_worker, args=(15, ))
#     process1.start()
#     process2.start()