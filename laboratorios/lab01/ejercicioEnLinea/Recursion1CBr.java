public int bunnyEars(int bunnies) {
    if(bunnies==0){ // C1 = 3
      return 0; 
    }
    else{                                   // T(n) = C2 + T(n-1)  
      return bunnyEars(bunnies-1)+2;        // C2=3
    }
}
/*Worst case
T(n) = C2 + T(n-1)  
Recurrence equation solution = c2n +c 
O(c2n +c) = O(n+c) ---> Regla del producto
O(n) ---> Regla de la suma 
O(n)
*/

public int triangle(int rows) {
    if(rows==0){    // C1= 3
         return 0; 
} else if (rows==1){ //C2=C1
    return 1; 
  } else{                                   // T(n) = C3+T(n-1)
        return triangle(rows-1)+rows;      //  C3=C1
    }
}
/*Worst case
T(n) = C2 + T(n-1)  
Recurrence equation solution = c2n +c 
O(c2n +c) = O(n+c) ---> Regla del producto
O(n) ---> Regla de la suma
O(n)
*/

public int bunnyEars2(int bunnies)
{
	if(bunnies == 0)    //C1=3
		return 0; 
	if(bunnies % 2 == 1)                        //T(n) = C2 + T(n-1)
		return 2 + bunnyEars2(bunnies-1);   // C2 = 6
	return 3 + bunnyEars2(bunnies-1);           // T(n) = C3 + T(n-1),  C3 = C1
}
/*Worst case
T(n) = C2 + T(n-1)  
Recurrence equation solution = c2n +c 
O(c2n +c) = O(n+c) ---> Regla del producto
O(n) ---> Regla de la suma
O(n)
*/

public int sumDigits(int n) {
  if(n < 10){        //C1= 3
	return n;
  }
	return sumDigits(n/10) + n%10;  //T(n) = C2 + T(n/10) , C2 = C1
}
/*Worst case
T(n) = C2 + T(n/10)
Recurrence equation solution = (c1*log(n))/log(10)+ C1
O((c1*log(n))/log(10)+ C1) = O((c1*log(n))/log(10)) ---> Regla de la suma
O((c1*log(n))/log(10)) = O(log(n))   ---> Regla del producto
O(log(n))


*/

public int fibonacci(int n) {
  if(n==0){          // C1=3
    return 0;
  }
  else if(n==1){   //C2=C1
    return 1;
  }
  else{                                   //T(n) = C3 + T(n-2) + T(n-1) 
    return fibonacci(n-2)+fibonacci(n-1); //C3 = 4
  }
}
/*Worst case
Recurrence equation solution = -C+C*Fn+C*Ln 
O(2^n)
*/

