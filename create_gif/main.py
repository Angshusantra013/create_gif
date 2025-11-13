import imageio.v3 as iio


def main():
    filename = ['chicklet1.png', 'chicklet2.png', 'chicklet3.png', 'chicklet4.png']
    images = [] 
    for i in filename:
        images.append(iio.imread(i))

    iio.imwrite('chicklet.gif', images, duration = 500, loop = 0)
    print("Gif created successfully!")


if __name__ == "__main__":
    main()
