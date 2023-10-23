
import math


def main() :
    
    triangle = []
    #triangle.append([3])
    #triangle.append([7, 4])
    #triangle.append([2,4,6])
    #triangle.append([8,5,9,3])
    triangle.append([75])
    triangle.append([95, 64])
    triangle.append([17,47,82])
    triangle.append([18, 35, 87, 10])
    triangle.append([20, 4, 82, 47, 65])
    triangle.append([19, 1, 23, 75, 3, 34])
    triangle.append([88, 2, 77, 73, 7, 63, 67])
    triangle.append([99, 65, 4, 28, 6, 16, 70, 92])
    triangle.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
    triangle.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
    triangle.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
    triangle.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
    triangle.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
    triangle.append([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
    triangle.append([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])

    #cust_print(triangle)

    i = len(triangle)
    totals_row = []

    current_index = 0
    current_value = triangle[0][current_index]
    total = current_value

    for row in triangle:
        next_row = i - 1

        if ( next_row -1 ) <= len(triangle):
            # start at the beginning of the row.
            current_index = 0

            for number in row:
                row_length = len(row)

                print(f"current row- {i}")
                print(f"current value - {current_value}")

                left_index = current_index 
                left_option = triangle[next_row][left_index]
                
                right_index = current_index + 1 if current_index + 1 <= row_length else current_index
                right_option = triangle[next_row][right_index]

                print(f"left  option - {left_option}")
                print(f"right option - {right_option}")

                current_index = left_index if left_option > right_option else right_index
                current_value = triangle[next_row][current_index]

                total = total + current_value

                totals_row.append(total)

                print(f"Choosing {current_value} as it is bigger.")
                print(f"New total is {total}")
                print(f" ")

                current_index += 1
            # end for number loop
            
        i -= 1
    # end for row loop

    print(f"total is: {total}")


# end main. 



def cust_print(triangle):
    max_length = 0
    row_length = 0

    for row in triangle:
        row_length = len(row) * 2
        #print(row_length)
        max_length = row_length if row_length > max_length else max_length

    for row in triangle:
        row_length = len(row) * 2
        row_str = ''

        for x in range (math.ceil((max_length - row_length) / 2)):
            row_str = ' ' + row_str
        for x in row: 
            str_x = '0' + str(x) if len(str(x)) < 2 else str(x)
            row_str = row_str + str_x + ' '
        print(row_str)
# end cust_print.         

main()
