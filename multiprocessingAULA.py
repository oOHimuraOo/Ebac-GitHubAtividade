import multiprocessing

results = []

def calc_square(numbers):
    global results
    for i in numbers:
        print('squar: ', str(i*i))
        results.append(i*i)
        print(f'within a result: {results}')

if __name__ == '__main__':
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p1.start()
    p1.join()
    print(f'result: {str(results)}')
    print('success')