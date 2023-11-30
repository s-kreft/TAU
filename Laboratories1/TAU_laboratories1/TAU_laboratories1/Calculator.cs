using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TAU_laboratories1
{
    internal class Calculator
    {
        char actionSign;
        double firstNum;
        double secondNum;
        public Calculator() 
        {
            ControlPanel();
        }
        public void ControlPanel()
        {
            Console.WriteLine("Welcome to calculator. Choose an action: Sum = '+', Subtract = '-', Multiply = '*', Division = '/', quit = 'q'");
            actionSign = char.Parse(Console.ReadLine());
            Console.WriteLine("Write first number");
            firstNum = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Write second number");
            secondNum = Convert.ToDouble(Console.ReadLine());

            do
            {
                switch (actionSign)
                {
                    case ('+'):
                        Console.WriteLine("Resoult is: ");
                        Console.WriteLine(Sum(firstNum, secondNum));                        
                        break;

                    case ('-'):
                        Console.WriteLine("Resoult is: ");
                        Console.WriteLine(Subtract(firstNum, secondNum));
                        break;

                    case ('*'):
                        Console.WriteLine("Resoult is: ");
                        Console.WriteLine(Multiply(firstNum, secondNum));
                        ;
                        break;

                    case ('/'):
                        Console.WriteLine("Resoult is: ");
                        Console.WriteLine(Division(firstNum, secondNum));
                        break;
                }
            }
            while (actionSign == 'q');
            {
                System.Environment.Exit(0);
            }

        }

        public double Sum(double firstNum, double secNum)
        {
            return firstNum + secNum;
        }
        public double Subtract(double firstNum, double secNum)
        {
            return firstNum - secNum;
        }
        public double Multiply(double firstNum, double secNum)
        {
            return firstNum * secNum;
        }
        public double Division(double firstNum, double secNum)
        {
           return firstNum / secNum;
        }
    }
}
