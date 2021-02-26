public int bunnyEars(int bunnies) {
    if(bunnies==0){ 
      return 0; 
    }
    else{
      return bunnyEars(bunnies-1)+2; 
    }
}

public int triangle(int rows) {
    if(rows==0){ 
         return 0; 
} else if (rows==1){ 
    return 1; 
  } else{
        return triangle(rows-1)+rows;
    }
}

public int bunnyEars2(int bunnies)
{
	if(bunnies == 0)
		return 0; 
	if(bunnies % 2 == 1)
		return 2 + bunnyEars2(bunnies-1); 
	return 3 + bunnyEars2(bunnies-1);
}

public int count7(int n) {
    if(n == 7){
     return 1;
   }else if(n < 10 && n != 7){
     return 0;
   }
   else{
     return count7(n%10)+count7(n/10);// T(n)= c + T(n%10) + T(n/10)
   }
 }

 public int powerN(int base, int n) {
  if(n==1){ 
    return base;
  } 
 return base*powerN(base,(n-1));
}
  