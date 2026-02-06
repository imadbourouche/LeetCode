package main

import (
	"fmt"
	"sort"
)

type Interval struct {
   start int
   end   int
}

func canAttendMeetings(intervals []Interval) bool {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].start < intervals[j].start 
	})

	for i := range intervals {
		if i == len(intervals) - 1 {
			break
		}
		if intervals[i].end > intervals[i+1].start {
			return false
		}
	}
	return true
}


func main() {
	intervals := []Interval{
		{start: 0, end: 5},
		{start: 5, end: 10},
		{start: 10, end: 20},
	}

	fmt.Println(canAttendMeetings(intervals))
}