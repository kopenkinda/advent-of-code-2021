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

def step2_helper(info: List[Long], steps: Int): Long = {
  if (steps <= 0) {
    val reduced = info.reduce((a, b) => a + b)
    return reduced
  }
  val newList = List(
    info(1), // 0
    info(2), // 1
    info(3), // 2
    info(4), // 3
    info(5), //  4
    info(6), // 5
    info(7) + info(0), // 6
    info(8), // 7
    info(0) // 8
  )
  return step2_helper(newList, steps - 1)
}

def step2(list: List[Int], steps: Int): Long = {
  val initial = List(
    list.filter(x => x == 0).size.toLong,
    list.filter(x => x == 1).size.toLong,
    list.filter(x => x == 2).size.toLong,
    list.filter(x => x == 3).size.toLong,
    list.filter(x => x == 4).size.toLong,
    list.filter(x => x == 5).size.toLong,
    list.filter(x => x == 6).size.toLong,
    list.filter(x => x == 7).size.toLong,
    list.filter(x => x == 8).size.toLong
  )
  return step2_helper(initial, steps)
}

step1(data, 9)
step2(data, 256)
