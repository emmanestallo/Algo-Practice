#include<iostream>
#include<string>

using namespace std;

void insertSort(int arr[], int n){
    //Imagine a deck of cards. You look at a certain card, let it be the key. 
    //To arrange the cards from least to greatest, we compare them pairwise 

    int i, j, key; 
    
    //Start at the 2nd element of the array, arr[1]. 
    for (j=1; j<n; j++){
        key = arr[j];
        i = j-1;
        //If the previous element is larger than the preceeding element, swap the two elements
        while (i>=0 && arr[i]>key){
            arr[i+1] = arr[i];
            i -= 1;
        }
        //Place the key at the proper position
        arr[i+1] = key; 
    }
}

//Create the merge algorithm 

void merge(int *arr, int s, int e){
    int mid = (s+e)/2;
    
    int i = s;
    int j = mid + 1;
    int k = s; 

    int temp[100];

    while (i<=mid && j<=end){
        if (arr[i] < arr[j]){
            temp[k++] = arr[i++];
        }
        else{
            temp[k++] = arr[j++];
        }
    }
    
    //To ensure that the left array has no pending elements
    while (i<=mid){
        temp[k++] = arr[i++];
    } 
    
    //To ensure that the right array has no pending elements
    while (j<=end){
        temp[k++] = arr[j++];
    }

    //Finally, copy all elements to the original array
    for(int i=s; i<=e; i++){
        arr[i] = temp[i];
    }

}


void mergeSort(int arr[], int s, int e){
    //Divide and conquer approach. First we divide, then sort, then merge.

    //s = start
    //e = end

    //Base case - if there is only 1 element or none at all.
    if (s>=e){
        return;
    }

    //Step 1: Divide
    int mid = (s+e)/2;

    //Step 2: Recursively sort the arrays
    mergeSort(arr, s, mid);
    mergeSort(arr, mid+1, e); 

    //Step 3: Merge the two arrays
    merge(arr,s,e); 


}
