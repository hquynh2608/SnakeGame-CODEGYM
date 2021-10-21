def input_data(ref):
    while True:
        try:
            num = int(input("Nhập một số: "))
            if num > ref:
                return num
                break
            else:
                print("Nhập một số dương lớn hơn {}".format(ref))
                print
        except ValueError:
            print("Bạn phải nhập một số nguyên!")
            print()

if __name__ == '__main__':
    start_num = input_data(0)
    end_num = input_data(start_num)
    for i in range(start_num,end_num+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)