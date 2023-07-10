class Solution:
    def operate_num(self,n1,n2,ex):
        if ex == '/':
            return int(n2/n1)
        elif ex == '*':
            return n2*n1
        elif ex == '+':
            return n2+n1
        elif ex == '-':
            return n2-n1

    def evalRPN(self, tokens) -> int:
        exp_stack = []
        operators = ["*","/","+","-"]
        for ele in tokens:
            if ele in operators:
                n1 = exp_stack.pop()
                n2 = exp_stack.pop()
                val = self.operate_num(int(n1),int(n2),ele)
                exp_stack.append(str(val))
            else:
                exp_stack.append(ele)
        return int(exp_stack[0])


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution()
print(sol.evalRPN(tokens))
