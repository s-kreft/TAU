using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

    
    namespace TAU_laboratories1
    {
        class Program
        {
            static void Main(string[] args)
            {
                Console.WriteLine("Type 1 to Start THE Program");
                int Start = int.Parse(Console.ReadLine());

                do
                {
                    Console.WriteLine("Type 1 to Start or Restart the program or type -1 to Exit the program");
                    int firstNum;
                    int secNum;
                    int thirdNum;
                    int Discriminant;
                    double x1;
                    double x2;
                    int sum;
                    char sign;
                    Console.WriteLine("Chose your sign (+,-,*,/) or type S for Square Equations");
                    sign = char.Parse(Console.ReadLine());
                    //Code for a + b
                    if (sign == '+')
                    {
                        Console.WriteLine("Type first number");
                        firstNum = int.Parse(Console.ReadLine());
                        Console.WriteLine("Type second number");
                        secNum = int.Parse(Console.ReadLine());
                        sum = firstNum + secNum;
                        Console.WriteLine("Your sum of {0} + {1} = {2}", firstNum, secNum, sum);

                    }
                    //Code for a - b
                    if (sign == '-')
                    {
                        Console.WriteLine("Type first number");
                        firstNum = int.Parse(Console.ReadLine());
                        Console.WriteLine("Type second number");
                        secNum = int.Parse(Console.ReadLine());
                        sum = firstNum - secNum;
                        Console.WriteLine("Your sum of {0} - {1} = {2}", firstNum, secNum, sum);

                    }
                    //Code for a * b
                    if (sign == '*')
                    {
                        Console.WriteLine("Type first number");
                        firstNum = int.Parse(Console.ReadLine());
                        Console.WriteLine("Type second number");
                        secNum = int.Parse(Console.ReadLine());
                        sum = firstNum * secNum;
                        Console.WriteLine("Your sum of {0} * {1} = {2}", firstNum, secNum, sum);

                    }
                    //Code for a / b
                    if (sign == '/')
                    {
                        Console.WriteLine("Type first number");
                        firstNum = int.Parse(Console.ReadLine());
                        Console.WriteLine("Type second number");
                        secNum = int.Parse(Console.ReadLine());
                        sum = firstNum / secNum;
                        Console.WriteLine("Your sum of {0} / {1} = {2}", firstNum, secNum, sum);

                    }
                    if (sign == 'S')                      //Code for square equations
                    {
                        Console.WriteLine("Type first number");
                        firstNum = int.Parse(Console.ReadLine());
                        Console.WriteLine("Type second number");
                        secNum = int.Parse(Console.ReadLine());
                        Console.WriteLine("Type third number");
                        thirdNum = int.Parse(Console.ReadLine());
                        Discriminant = secNum * secNum - (4 * firstNum * thirdNum);
                        Console.WriteLine("Your Discriminant is {0}", Discriminant);

                        if (Discriminant > 0)
                        {
                            double squareRoot = Math.Sqrt(Discriminant);
                            double a = firstNum;
                            double b = secNum;
                            double c = thirdNum;
                            x1 = (-secNum - squareRoot) / (2 * firstNum);
                            x2 = (-secNum + squareRoot) / (2 * firstNum);
                            Console.WriteLine("Your First X is {0} and Your Second X is {1}", x1, x2);
                        }
                        if (Discriminant == 0)
                        {
                            double squareRoot = Math.Sqrt(Discriminant);
                            double a = firstNum;
                            double b = secNum;
                            double c = thirdNum;
                            x1 = (-secNum) / (2 * firstNum);
                            Console.WriteLine("Your First X and your Second X is {0}", x1);
                        }
                        if (Discriminant < 0)
                        {
                            Console.WriteLine("There are not real square equations");

                        }


                    }
                } while (Start == 1);


            }
        }
    }
