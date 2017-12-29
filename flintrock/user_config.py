
java_installer = """
        echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
    """

python_cmd = "python3"
install_cmd = "apt-get --assume-yes"

