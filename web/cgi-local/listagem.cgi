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
use MIME::Base64;

require 'C:\xampp\htdocs\Repositorio\diversos\movies\cgi-local\conexao.cgi';
mysql();

print "Content-type: text/html \n\n";

my $cgi = new CGI();

$funcao = $cgi->param('funcao');
$id = $cgi->param('id');
$status = $cgi->param('status');

print $status;

if(!$funcao) {
	my @lista;
	my $json = "";

	#my $dbh = DBI->connect($dsn, $userid, $password) or die $DBI::errstr;
	my $sth = $dbh->prepare("SELECT id,nome, preco, tipo, img, status FROM filmes order by id desc");
	$dir = 'img/';
	$sth->execute();

	 while (my ($id, $nome, $preco, $tipo, $img, $status) = $sth->fetchrow_array) {
		
		if($status eq 1) {
			$new_status = JSON::true;
		}else {
			$new_status = JSON::false;
		}

		push @lista, {
			'filme_id' => $id,
	        'filme_nome' => $nome,
	        'filme_preco' => $preco,
	        'filme_tipo' => $tipo,
	        'filme_img' => $dir.$img,
	        'status' => $new_status, 
	        'status_id' => $status,
	    };

	}
	$json = JSON->new->allow_nonref;
	print $json->encode( \@lista );

}elsif($funcao eq 'excluir') {
	if ($status eq 'false') {
		$valor = 1;
	} else {
		$valor = 2;
	}
	my $sth = $dbh->prepare("UPDATE filmes SET status= $valor where id = $id");
	$sth->execute();

	print "UPDATE filmes SET status= $valor where id = $id";



}