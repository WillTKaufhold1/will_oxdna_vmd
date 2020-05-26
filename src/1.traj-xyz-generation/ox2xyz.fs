open System.IO
open System

let main args = 

    let mutable top_fname = ""
    let mutable dat_fname = ""
 
    //top_fname <- args.[0]
    //dat_fname <- args.[1]
    
    // let's take the dat file and then the top file as args, then a string indicating some preferences

    use sr_top = new StreamReader ("top")
    let first_line = sr_top.ReadLine()
    let N_part = first_line.Split(' ').[0]

    use sr = new StreamReader ("dat")
    let mutable line = ""
    let mutable X_ = "" 
    let mutable Y_ = ""  
    let mutable Z_ = ""

    let mutable X = 1.
    let mutable Y = 1.  
    let mutable Z = 1.

    let mutable bX_ = ""
    let mutable bY_ = ""
    let mutable bZ_ = ""

    let mutable bX = 1.
    let mutable bY = 1.
    let mutable bZ = 1.

    let mutable cX_ = ""
    let mutable cY_ = ""
    let mutable cZ_ = ""

    let mutable cX = 1.
    let mutable cY = 1.
    let mutable cZ = 1.


    let mutable localline = ""

    let delta = 586.992248

    while not sr.EndOfStream do

        line <- sr.ReadLine () 
        if line.[0..2] = "t =" then 
            System.Console.WriteLine(string ( (int N_part ) * 2 ) ) 
        elif line.[0..2] = "b =" then
            System.Console.WriteLine("#molecule")
        elif line.[0..2] <> "E =" then


            X_ <- (line.Split ' ').[0] 
            Y_ <- (line.Split ' ').[1] 
            Z_ <- (line.Split ' ').[2] 

            bX_ <- (line.Split ' ').[3] 
            bY_ <- (line.Split ' ').[4] 
            bZ_ <- (line.Split ' ').[5] 

            cX_ <- (line.Split ' ').[6] 
            cY_ <- (line.Split ' ').[7] 
            cZ_ <- (line.Split ' ').[8] 


            X <- float X_
            Y <- float Y_
            Z <- float Z_
            
            bX <- float bX_ 
            bY <- float bY_
            bZ <- float bZ_
 
            cX <- float cX_ 
            cY <- float cY_
            cZ <- float cZ_


            while X < 0. do           
                X <- X + delta
            while Y < 0. do           
                Y <- Y + delta
            while Z < 0. do           
                Z <- Z + delta

            X_ <- string (X - 0.4 * bX) 
            Y_ <- string (Y - 0.4 * bY)
            Z_ <- string (Z - 0.4 * bZ)
            localline <- "O " + X_ + " " + Y_ + " " + Z_
            System.Console.WriteLine(localline)

            X_ <- string (X + 0.4 * bX + cX*0.34) // this is the stacking site.
            Y_ <- string (Y + 0.4 * bY + cY*0.34) // NB: all of these interaction values come from the model.h file.kj
            Z_ <- string (Z + 0.4 * bZ + cZ*0.34)
            localline <- "C " + X_ + " " + Y_ + " " + Z_

            System.Console.WriteLine(localline)
                
main()









    
