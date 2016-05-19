class openblas(Wig):
	tarball_uri = 'https://github.com/xianyi/OpenBLAS/archive/v$RELEASE_VERSION$.tar.gz'
	last_release_version = 'v0.2.18'
	supported_features = ['debug']

	def setup(self):
		self.skip('configure')
		self.make_flags += ['FC=gfortran', 'NO_AFFINITY=1', 'USE_OPENMP=1']
		self.make_install_flags += [S.PREFIX_MAKE_INSTALL_FLAG]
	
	def switch_debug_on(self):
		self.make_flags += ['DEBUG=1']
