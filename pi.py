# -*- coding: utf-8 -*-
from __future__ import division
####################导入时间模块
import time

try:
    def pi(inputNumber):
        ################算法根据马青公式计算圆周率####################

        number = int(inputNumber)

        ###############计算当前时间
        time1 = time.time()

        # 多计算10位，防止尾数取舍的影响
        number1 = number + 10

        # 算到小数点后number1位
        b = 10 ** number1

        # 求含4/5的首项
        x1 = b * 4 // 5
        # 求含1/239的首项
        x2 = b // -239

        # 求第一大项
        he = x1 + x2
        # 设置下面循环的终点，即共计算n项
        number *= 2

        # 循环初值=3，末值2n,步长=2
        for i in xrange(3, number, 2):
            # 求每个含1/5的项及符号
            x1 //= -25
            # 求每个含1/239的项及符号
            x2 //= -57121
            # 求两项之和
            x = (x1 + x2) // i
            # 求总和
            he += x

        # 求出π
        pai = he * 4
        # 舍掉后十位
        pai //= 10 ** 10

        ############ 输出圆周率π的值
        paistring = str(pai)
        result = paistring[0] + str('.') + paistring[1:len(paistring)]
        print result

        time2 = time.time()
        print u'总共耗时：' + str(time2 - time1) + 's'
        return result, str(time2 - time1)


    if __name__ == "__main__":
        output = pi(raw_input("Please input a number you want:"))
        print output
except ValueError:
    print "Triggered Value Error.\nIs that a vaild input?"
    exit(1)
