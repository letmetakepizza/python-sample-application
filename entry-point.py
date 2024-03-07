from pythonapp import func_1, func_2, class_1

def main():
    vec = [10, 20, 30, 40, 50]
    print(f"Average: {func_1.avg(vec)}")

    x = [[1, 2, 3], [4, 5, 6]]
    print(f"Dimensions: {func_2.dim(x)}")

    my_car = class_1.Car("Tesla", 2021, "blue")
    my_car.drive(150)
    my_car.description("My car")

if __name__ == "__main__":
    main()
