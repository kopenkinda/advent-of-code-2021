import scala.io.Source
val xd = Source.fromFile("./01.input").getLines.toList.map(_.toInt)

// Github Copilot's solution
val b = xd.sliding(2).map(x => if (x.head > x.last) 0 else 1).sum


// # George's solution
def pog(l : List[Int], n : Int, c : Int) : Int = l match {
    case Nil => c
    case x :: xs =>
        if (x > n) pog(xs, x, c+1)
        else pog(xs, x, c)
}
val res = pog(xd.tail, xd.head, 0)

def pog2(l : List[Int], n : Int, c : Int) : Int = l match {
    case x :: y :: z :: xs =>
        if (z > n) pog2(y :: z :: xs, x, c+1)
        else pog2(y :: z :: xs, x, c)
    case _ => c
}

val res2 = pog2(xd.tail, xd.head, 0)