chr_test = c(2,4)

pop_test = matrix(sample(9,12,replace=T), ncol=2)

population <- function(n,l){
  return(matrix(nrow=n,ncol=l,0))
}

fitness <- function(chr){
  x<-chr[1];
  y<-chr[2];
  return(x*sin(4*x)+1.1*y*sin(2*y))
}

mutation <- function(chr){
  ran_locus <- sample(1:length(chr),1);
  v<-chr[ran_locus];
  new_value<-rnorm(1,v,0.1);
  while(new_value < 0 || new_value > 10){
    new_value<-rnorm(1,v,0.1);
  }
  new_chr <- chr;
  new_chr[ran_locus]<-new_value;
  return(new_chr)
  }

selection  <- function(population,elitism){
  sorted <- order(population[,ncol(population)]);
  return(sorted[1:(nrow(population)*elitism)])
  }

recombination <- function(ch1,ch2){
  B <- runif(length(ch1));
  OFF1 <- ch1*B+(1-B)*ch2;
  OFF2 <- ch1*(1-B)+B*ch2;
  OFFS <- matrix(ncol=length(OFF1),nrow=2);
  OFFS[1,]<-OFF1;
  OFFS[2,]<-OFF2;
  return(OFFS)
}

mating <- function(population,best){
  new_pop <- population(nrow(population),ncol(population));
  new_pop[1:length(best),] = population[best,];
  for (i in (length(best)+1) : nrow(new_pop)){
    parents <- best[sample(2,length(best),replace=T)];
    OFFs <- recombination(population[parents[1],],population[parents[2],]);
    mutation(OFFs[sample(1,2,replace=T)]);
    new_pop[i:(i+1),] <- OFFs
  }
  return(new_pop);
}

add_fit <- function(pop){
  c <- matrix(nrow=nrow(pop),ncol=1);
  for (i in 1:nrow(pop)){
    c[i,]=fitness(pop[i,])
  }
  return(cbind(pop,c))
}