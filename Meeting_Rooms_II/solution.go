package main

import (
	"sort"
	"fmt"
)

type Interval struct {
	start int
	end   int
}


func minMeetingRooms(intervals []Interval) int {
	if len(intervals) == 0{
		return 0
	}
	
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].start < intervals[j].start
	})
	buckets := []int{intervals[0].end}
	for i := 1; i < len(intervals); i++ {
		found_bucket := false
		for j := range buckets {
			if intervals[i].start >= buckets[j] {
				buckets[j] = intervals[i].end
				found_bucket = true
				break
			}
		}
		if !found_bucket {
			buckets = append(buckets, intervals[i].end)
		}
	}
	return len(buckets)
}

func main() {
	intervals := []Interval{
		{start: 0, end: 30},
		{start: 5, end: 10},
		{start: 15, end: 20},
	}
	fmt.Println(minMeetingRooms(intervals)) // Output: 2
}