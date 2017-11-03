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

sub EscolheAcao{
  my($var) = @_;
  #use v5.10.1;
  if ($var eq 'listarFilmes') {
  	&listarFilmes();
  } elsif ($var eq 'logar') {
  	&logar();
  } elsif ($var eq 'inserir') {
  	&inserir();
  }
}


sub logar {
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
			'valido' => true
		});
		exit;
	}

	$json = JSON->new->allow_nonref;
	print $json->encode( {
		'valido' => false
	});

}


sub inserir {
	
	my $j = JSON->new;

	my %dados = %{$j->decode($cgi->param('POSTDATA'))};

	my $nome = $dados{'nome'};
	my $preco = $dados{'preco'};
	my $tipo = $dados{'tipo'};
	my $img = $dados{'img'};

	my $sth = $dbh->prepare("INSERT INTO filmes(nome, preco, tipo, img) VALUE ('$nome', '$preco', '$tipo', '$img')");
	$sth->execute() or die $DBI::errstr;
}

sub listarFilmes {

	my @lista;
	my $json = "";

	#my $dbh = DBI->connect($dsn, $userid, $password) or die $DBI::errstr;
	my $sth = $dbh->prepare("SELECT nome, preco, tipo, img FROM filmes");

	$sth->execute();

	 while (my ($nome, $preco, $tipo, $img) = $sth->fetchrow_array) {
		
		push @lista, {
	        'filme_nome' => $nome,
	        'filme_preco' => $preco,
	        'filme_tipo' => $tipo,
	        'filme_img' => $img
	    };

	}
	$json = JSON->new->allow_nonref;
	print $json->encode( \@lista );
}

if ($cgi->param('POSTDATA') ne undef) {
	$json = JSON->new->allow_nonref;
    my %dados = %{$json->decode($cgi->param('POSTDATA'))};

    my $funcao = $dados{'sub'};

    &EscolheAcao($funcao);
} else {
	&EscolheAcao($cgi->param('sub'));
}
&EscolheAcao($cgi->param('sub'));