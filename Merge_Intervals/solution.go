package main

import (
	"sort"
	"fmt"
)


func merge(intervals [][]int) [][]int {
	sort.Slice(intervals, func (i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
    res := [][]int {
		intervals[0],
	}
	j := 0
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] <= res[j][1] {
			if intervals[i][1] > res[j][1]{
				res[j][1] = intervals[i][1]
			}
		}else{
			res = append(res, intervals[i])
			j += 1
		}
	}
	return res
}


func main(){
	intervals := [][]int {
		{1, 3},
		{2, 6},
		{8, 10},
		{15, 18},
	}
	fmt.Println(merge(intervals))
}
