from PIL import Image
from matrices import image_to_matrix, rotate_matrix, scale_matrix, skew_matrix, to_grayscale, edge_detection, matrix_to_image

def main():
    filename = input("Enter image filename: ")
    try:
        img = Image.open(filename)
    except:
        print("File not found.")
        return

    channels = image_to_matrix(img)

    print("Choose a transformation")
    print("1. Rotate")
    print("2. Scale")
    print("3. Skew")
    print("4. Grayscale")
    print("5. Edge Detection")
    choice = input("Insert the option you want: ")

    out_channels = []

    if choice == '1':
        angle = float(input("Insert many degrees to you want to rotate your image: "))
        cx = int(input("Insert the X center (column): "))
        cy = int(input("Insert the Y center (row): "))
        for c in channels:
            out_channels.append(rotate_matrix(c, (cx, cy), angle))

    elif choice == '2':
        factor = float(input("Scale factor: "))
        for c in channels:
            out_channels.append(scale_matrix(c, factor))

    elif choice == '3':
        sx = float(input("Skew X factor: "))
        sy = float(input("Skew Y factor: "))
        for c in channels:
            out_channels.append(skew_matrix(c, sx, sy))

    elif choice == '4':
        gray_mat = to_grayscale(channels[0], channels[1], channels[2])[0]
        out_channels = [gray_mat, gray_mat, gray_mat]

    elif choice == '5':
        threshold = int(input("Edge detection threshold (between 1 and 255): "))
        gray_mat = to_grayscale(channels[0], channels[1], channels[2])[0]
        edge_mat = edge_detection(gray_mat, threshold)
        out_channels = [edge_mat, edge_mat, edge_mat]

    else:
        print("Invalid option.")
        return

    output_image = matrix_to_image(out_channels[0], out_channels[1], out_channels[2])
    output_image.show()

    output_name = input("Save as (filename): ")
    output_image.save(output_name)
    print("Image saved successfully.")

main()