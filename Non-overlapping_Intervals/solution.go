package main

import (
	"sort"
	"fmt"
)

func eraseOverlapIntervals(intervals [][]int) int {
    if len(intervals) <= 1 {
        return 0
    }

    res := 0
    
    sort.Slice(intervals, func (i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })

    i := 0
    j := 1
    for j < len(intervals) {
        if intervals[i][1] > intervals[j][0] {
            res += 1
            if intervals[i][1] > intervals[j][1]{
                i = j
            }
        } else {
            i = j
        }
        j += 1
    }

    return res
}



func main(){
	intervals := [][]int {
		{1,2},
		{2,4},
		{1,4},
	}
	fmt.Println(eraseOverlapIntervals(intervals))
}
