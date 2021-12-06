import scala.io.Source
val data = Source
  .fromFile("./06.input")
  .mkString
  .split(",")
  .map(x => x.toInt)
  .toList

def step1(list: List[Int], steps: Int): Int = {
  if (steps == 0) {
    return list.size
  }
  val toEnd = list.filter(x => x == 0).map(x => 8)
  val others = list.map(x => if (x > 0) x - 1 else 6)
  step1(others ++ toEnd, steps - 1)
}

def step2(list: List[Int], steps: Int): Int = {
  if (steps == 0) {
    return list.size
  }
  val toEnd = list.filter(x => x == 0).map(x => 8)
  val others = list.map(x => if (x > 0) x - 1 else 6)
  step2(others ++ toEnd, steps - 1)
}

step1(data, 80)
