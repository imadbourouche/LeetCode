package main

import (
	"container/heap"
	"fmt"
	"sort"
)

type Interval struct {
	start int
	end   int
}

// MinHeap implements a min-heap for meeting end times
type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minMeetingRooms(intervals []Interval) int {
	if len(intervals) == 0 {
		return 0
	}

	// Step 1: Sort intervals by start time
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].start < intervals[j].start
	})

	// Step 2: Initialize min-heap and push first meeting end time
	h := &MinHeap{}
	heap.Init(h)
	heap.Push(h, intervals[0].end)

	// Step 3: Iterate remaining meetings
	for i := 1; i < len(intervals); i++ {
		if intervals[i].start >= (*h)[0] {
			// Reuse room: remove earliest ending meeting
			heap.Pop(h)
		}
		// Add current meeting's end time
		heap.Push(h, intervals[i].end)
	}

	// Step 4: Number of rooms = heap size
	return h.Len()
}


func main() {
	intervals := []Interval{
		{start: 0, end: 30},
		{start: 5, end: 10},
		{start: 15, end: 20},
	}
	fmt.Println(minMeetingRooms(intervals)) // Output: 2
}