import scala.io.Source
import scala.language.postfixOps

val data = Source
  .fromFile("./04.input")
  .getLines
  .toList

val numbers = data.head.split(',').toList.map((x) => x.toInt).toList
val tables = data.tail.tail
  .mkString("#")
  .split("##")
  .toList
  .map((x) =>
    x.split("#")
      .toList
      .map((x) =>
        x.split(" ")
          .filter((y) => y != "")
          .map((y) => y.toInt)
          .toList
      )
  )

def transpose(m: List[List[Int]]): List[List[Int]] = {
  (0 until m.head.size toList) map { c =>
    (0 until m.size toList) map { r =>
      m(r)(c)
    }
  }
}
def reverseRows(m: List[List[Int]]): List[List[Int]] = m.map(_.reverse)
def rotateBy90ClockWise(m: List[List[Int]]): List[List[Int]] = reverseRows(
  transpose(m)
)

def reduceTable(table: List[List[Int]], played: List[Int]): Int = {
  val combined = table.reduce((acc, v) => acc ++ v)
  val filtered = combined.filter(x => !played.contains(x))
  val reduced = filtered.reduce((acc, v) => acc + v)
  return reduced
}

def isWinning(table: List[List[Int]], played: List[Int]): Boolean = {
  table.foreach(line => {
    val rest = line.filter(el => played.contains(el))
    if (rest.size == line.size) {
      return true
    }
  })
  val rotated = rotateBy90ClockWise(table)
  rotated.foreach(line => {
    val rest = line.filter(el => played.contains(el))
    if (rest.size == line.size) {
      return true
    }
  })
  return false
}

def step1(
    list: List[List[List[Int]]],
    nums: List[Int],
    played: List[Int]
): Int = {
  val current = nums.head
  val nextPlayed = current :: played
  list.foreach(table => {
    if (isWinning(table, nextPlayed)) {
      return current * reduceTable(table, nextPlayed)
    }
  })
  step1(list, nums.tail, nextPlayed)
}

step1(tables, numbers, Nil)

def step2(
    list: List[List[List[Int]]],
    nums: List[Int],
    played: List[Int]
): Int = {
  val current = nums.head
  val nextPlayed = played ++ List(current)
  if (list.size == 1 && isWinning(list.head, nextPlayed)) {
    return current * reduceTable(list.head, nextPlayed)
  }
  val filtered = list.filter(x => !isWinning(x, nextPlayed))
  step2(filtered, nums.tail, nextPlayed)
}

step2(tables, numbers, Nil)
