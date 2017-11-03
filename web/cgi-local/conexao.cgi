#!"c:\perl\bin\perl.exe"
use DBI;

sub mysql {

	my $driver = "mysql"; 
	my $database = "movies";
	my $dsn = "DBI:$driver:database=$database;host=localhost;port=3306";
	my $userid = "root";
	my $password = "";
	my @row = "";

	$dbh = DBI->connect($dsn, $userid, $password) or die $DBI::errstr;

};


1;