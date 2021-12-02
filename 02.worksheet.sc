import scala.io.Source
val data = Source
  .fromFile("./02.input")
  .getLines
  .toList
  .map(_.split(" ").toList)
  .map((x) => (x.head , x.last.toInt))

def part1(l : List[Tuple2[String, Int]], h : Int, v : Int) : Int = {
  if (l.isEmpty) {
    h * v
  } else {
    val (x, y) = l.head
    if (x == "up") {
      part1(l.tail, h, v - y)
    } else if (x == "down") {
      part1(l.tail, h, v + y)
    } else {
      part1(l.tail, h + y, v)
    }
  }
}

part1(data, 0, 0)


def part2(l : List[Tuple2[String, Int]], h : Int, a : Int, d: Int) : Int = {
  if (l.isEmpty) {
    h * d
  } else {
    val (x, y) = l.head
    if (x == "up") {
      part2(l.tail, h, a - y, d)
    } else if (x == "down") {
      part2(l.tail, h, a + y, d)
    } else {
      part2(l.tail, h + y, a, d + a * y)
    }
  }
}


part2(data, 0, 0, 0)
