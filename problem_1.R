n_unique_bdays <- function(n) {
	mean(replicate(1000, 
		sum(as.data.frame(table(sample(1:365, n, replace=TRUE)))$Freq == 1)))}

percent_identifiable <- function(n) {
	n_unique_bdays(n) / n }

read_and_calc <- function(csv_path){
	setAs("character", "num.with.commas", function(from) as.numeric(gsub(",", "", from) ) )
	csv <- read.csv(csv_path,
		colClasses=c('num.with.commas', 'num.with.commas'))
	reswomen <- sapply(csv$Women, n_unique_bdays)
	resmen <- sapply(csv$Men, n_unique_bdays)
	total_ident <- (sum(resmen) + sum(reswomen))
	total_pop <- sum(csv$Men) + sum(csv$Women)
	return(list("total_identified" = total_ident, "total_population"=total_pop, "frac"=(total_ident/total_pop)))
}


## Plot what proportion of people with the same age and zipcode 
## are identifiable as the number of people increases.
xs <- seq(1, 2000, 10)
res <- sapply(xs, percent_identifiable)
plot(xs, res, type='l')

## Calculate the total number of people identified, total population, 
## and percent of people identifiable for Cambridge, West Palm Beach, and Manhattan.

read_and_calc("westpalmbeach.csv")
read_and_calc("manhattan.csv")
read_and_calc("cambridge.csv")