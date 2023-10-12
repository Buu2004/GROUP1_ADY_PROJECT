#include <stdio.h>
void Sieve_of_Eratosthenes(int n);
main()
{
	Sieve_of_Eratosthenes(2);
}

void Sieve_of_Eratosthenes(int n)
{
	bool isPrime[n+1];
	for (int i=0; i<=(n+1); i++)
		isPrime[i] = true;
	
	int j=2;
	
	while ((j*j)<= n) {
		if (isPrime[j]) {
			int k;
			for (k=j*j; k <= n; k=k+j)
				isPrime[k] = false;
		}
		j+=1;
	}
	
	
	for (int m=2; m<=n; m++) {
		if (isPrime[m])
			printf("%d\n", m);
	}
	
}
