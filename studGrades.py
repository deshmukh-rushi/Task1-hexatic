# Write a Python program that stores student grades 
# in a list and calculates the average grade.
# If the average is above 50, print "Pass"; otherwise, print "Fail.

class PassFail:
    def __init__(self):
        self.marks_list = []
        print("Enter marks of 5 subjects:")
    
    def marks(self):
        for i in range(5):
            while True:
                try:
                    mark = int(input(f"Subject {i + 1}: "))
                    if mark < 0 or mark > 100:
                        print("Number out of range. Enter a mark between 0 and 100.")
                        continue
                    self.marks_list.append(mark)
                    break
                except ValueError:
                    print("Enter a valid integer.")
        
        print(f"Your marks for 5 subjects are: {self.marks_list}")
        
    def avg(self):
        
        average = sum(self.marks_list) / len(self.marks_list)
        print(f"Your average marks are: {average}")
        
        if average >= 50:
            print("Congratulations!! You passed.")
        else:
            print("Sorry, you failed.")


a = PassFail()
a.marks()
a.avg()