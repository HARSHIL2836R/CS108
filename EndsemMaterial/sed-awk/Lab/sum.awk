BEGIN{
	FS=",";
	OFS=",";
	net=0;
}
! /Week_end/{
	sum[$3] += $4;
	net += $4;
}
{
	print $0
}
END{
	print "=====";
	print "Net : "net;
	asorti(sum, sorted_sum);
	for (g in sorted_sum)
		for (v in sum)
			if (v == sorted_sum[g])
				print v" : "sum[v];
}
