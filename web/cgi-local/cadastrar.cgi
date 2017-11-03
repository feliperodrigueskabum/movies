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
use Encode qw(decode encode);

require 'C:\xampp\htdocs\Repositorio\diversos\movies\cgi-local\conexao.cgi';

mysql();

print "Content-type: text/html \n\n";

my $cgi = new CGI();

$CGI::POST_MAX = 100 * 1024;

my $nome = $cgi->param('filme_nome');
my $preco = $cgi->param('filme_preco');
my $tipo = $cgi->param('filme_tipo');
my $file = $cgi->param('filme_img');
my $id = $cgi->param('filme_id');






$fh = $cgi->upload('filme_img');
$dir = '../img/';
open FILE, ">$dir$file";

binmode(FILE);

while (<$fh>) {
    print FILE;
}

close FILE;


if($id == undef) {

	my $sth = $dbh->prepare("INSERT INTO filmes(nome, preco, tipo, img, status) VALUE ('$nome', '$preco', '$tipo', '$file', 1)");
	$sth->execute() or die $DBI::errstr;
	print ("INSERT INTO filmes(nome, preco, tipo, img, status) VALUE ('$nome', '$preco', '$tipo', '$file', 1)");

}else {

	my $sth = $dbh->prepare("UPDATE filmes set nome= '$nome', preco= '$preco', tipo= '$tipo', img= '$file' where id= $id");
	$sth->execute() or die $DBI::errstr;
	print "UPDATE filmes set nome= '$nome', preco= '$preco', tipo= '$tipo', img= '$file' where id= $id";

};