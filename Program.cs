using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CometPassword
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            string args =  "hello" ;
            run_python(args);
            Application.Run(new Form1());

        }

        public static void run_python(string args)
        {
            string fileName = @"..\\..\\tester.py";

           //Process p = new Process();
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = "C:/Python310/python.exe";//cmd is full path to python.exe
            start.Arguments = @"hello";//args is path to .py file and any cmd line args
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            start.CreateNoWindow = true;

            /*  p.StartInfo = new ProcessStartInfo(@"C:\\Python310\\python.exe")
              {
                  RedirectStandardOutput = true,
                  UseShellExecute = false,
                  CreateNoWindow = true,
                  FileName = fileName,
                  Arguments = string.Format("{0} {1}", @"r'C:/Users/super/Documents/UTD/Data Application and Security/CometPassword/CometPassword/CometPassword/tester.py'", args)

              };*/
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    Console.Write(result);
                }
            }
            //p.WaitForExit();

            /*            ProcessStartInfo start = new ProcessStartInfo();
                        start.FileName = "my/full/path/to/python.exe";
                        start.Arguments = string.Format("{0} {1}", cmd, args);
                        start.UseShellExecute = false;
                        start.RedirectStandardOutput = true;
                        using (Process process = Process.Start(start))
                        {
                            using (StreamReader reader = process.StandardOutput)
                            {
                                string result = reader.ReadToEnd();
                                Console.Write(result);
                            }
                        }*/
        }
    }
}
