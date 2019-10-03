%global srcname jupyter-console
%global srcname_ jupyter_console

Name:           python-%{srcname}
Version:        6.0.0
Release:        4%{?dist}
Summary:        Jupyter terminal console

License:        BSD
URL:            https://jupyter.org
Source0:        %pypi_source %{srcname_}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
An IPython-like terminal frontend for Jupyter kernels in any language.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  (python3dist(prompt-toolkit) >= 2 with python3dist(prompt-toolkit) < 2.1)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(pyzmq)

%{?python_enable_dependency_generator}

%description -n python3-%{srcname}
An IPython-like terminal frontend for Jupyter kernels in any language.


%package -n python-%{srcname}-doc
Summary:        jupyter-console documentation

BuildArch: noarch

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinxcontrib-github-alt)

%description -n python-%{srcname}-doc
Documentation for jupyter-console


%prep
%autosetup -n %{srcname_}-%{version}


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    nosetests-3 %{srcname_}


%files -n python3-%{srcname}
%doc README.md
%license COPYING.md
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname_}
%{python3_sitelib}/%{srcname_}-%{version}-py?.?.egg-info

%files -n python-%{srcname}-doc
%doc html
%license COPYING.md


%changelog
* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 6.0.0-1
- Initial package.
