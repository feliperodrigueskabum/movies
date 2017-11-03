#!"c:\perl\bin\perl.exe"
use CGI::Carp qw(fatalsToBrowser);
use Data::Dumper;
use File::Basename;
use HTML::Entities;
use XML::Simple qw(:strict);
use Try::Tiny;
use Time::Local;
use CGI;
use DBI;
use Data::Dumper;
use JSON;
use Encode qw(decode encode);

require 'C:\xampp\htdocs\Repositorio\diversos\movies\cgi-local\conexao.cgi';
mysql();

print "Content-type: text/html \n\n";

my $cgi = new CGI();

my $l = JSON->new;
my %dados = %{$l->decode($cgi->param('POSTDATA'))};
my @listaLogin;
my $json2 = "";


my $login = $dados{'login'};
my $pass = $dados{'senha'};

my $sth = $dbh->prepare("SELECT nome, senha FROM usuario where nome = '$login' and senha = '$pass'");
$sth->execute();

while (my ($nome, $senha) = $sth->fetchrow_array) {
	$json = JSON->new->allow_nonref;
	print $json->encode( {
		# $session = new CGI::Session("driver:File", undef, {Directory=>"/tmp"});
		# $sid = $session->id();
		'valido' => true
		#'id' => $sid
		});
	exit;
}

$json = JSON->new->allow_nonref;
print $json->encode( {
	'valido' => false
});

