import time
import threading

def calc_square(numbers):
    print('calculate square numbers: ')
    for i in numbers:
        #time - delay
        time.sleep(2)
        j = i*i
        print(f' square: {j}')

def calc_cube(numbers):
    print('calculate cube numbers: ')
    for i in numbers:
        time.sleep(2)
        j = i*i*i
        print(f' cube: {j}')

if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    t1 = threading.Thread(target=calc_square, args=(arr,))
    t2 = threading.Thread(target=calc_cube, args=(arr,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('Main thread here!!')
    print('Successes')
