using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Bernoull
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void input_m_TextChanged(object sender, EventArgs e)
        {
            ReCalculate();
        }

        /// <summary>
        /// Updates the answer output when one of the parameters changes
        /// </summary>
        private void ReCalculate()
        {
            int m = 0;
            int n = 0;
            double p = 0;
            double q = 0;

            Int32.TryParse(input_m.Text, out m);
            Int32.TryParse(input_n.Text, out n);
            Double.TryParse(input_p.Text, out p);
            Double.TryParse(input_q.Text, out q);

            answer.Text = CalculateBernoull(m, n, p, q).ToString();
        }

        /// <summary>
        /// Calculates the value according to Bernoull's formula
        /// </summary>
        /// <param name="m"></param>
        /// <param name="n"></param>
        /// <param name="p"></param>
        /// <param name="q"></param>
        /// <returns></returns>
        public double CalculateBernoull(int m, int n, double p, double q)
        {
            double answer = 0;
            
#region Validity checks
            bool is_valid = true;
            if (m > n || m < 0 || n < 0 || p <= 0 || q <= 0 || q >= 1 || p >=1 || (p + q) != 1)
            {
                is_valid = false;
            }

            if (!is_valid)
            {
                return 0;
            }
#endregion

            answer = Combination(n, m);
            answer *= Math.Pow(p, m);
            answer *= Math.Pow(q, (n-m));
            return answer;
        }


        public static double Factorial(double n)
        {
            if (n < 0) { throw new Exception("Cannot take the factorial of a negative number"); }
            double factorial = 1;
            // 0! and 1! = 1
            for (double i = 2; i < n + 1; i++)
            {
                factorial *= i;
            }
            return factorial;
        }

        /// <summary>
        /// Performs a nCr Combination of the two numbers
        /// </summary>
        /// <param name="n">The Number</param>
        /// <param name="r">The Range</param>
        /// <returns></returns>
        public static double Combination(double n, double r)
        {
            /*
             * Formula for Combination: n! / (r! * (n - r)!)
             */

            // n and r should be integral values
            double rfloor = Math.Floor(r);
            double nfloor = Math.Floor(n);
            // Check for all invalid values of n and r.
            if ((n < 1) || (r < 0) || (r > n) || (r != rfloor) || (n != nfloor))
            {
                throw new Exception("Invalid Input to Combination Function: Number must be greater than Range");
            }

            return Factorial(n) / (Factorial(r) * Factorial(n - r));
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("http://ando.roots.ee");
        }

    }
}
