class Solver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def m_solver(self):
        m_result = (float(self.c) + float(self.b))/float(self.a)
        return m_result

    #def p_solver(self, a, b,c):
      #  p_result = ((float(self.c**2)-float(self.b))/float(self.a)
       # return p_result

num_input = input("Enter values for a, b, and c in ax-b=c: ").split()
num1, num2, num3 = map(float, num_input)
x = Solver(num1,num2,num3)
calcmono=x.m_solver()
print(calcmono)

#calcpoly=Solver.p_solver(num1,num2,num3)
