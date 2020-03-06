## pxc volume inspect

Describe a Portworx volume

### Synopsis

Show detailed information of Portworx volumes

```
pxc volume inspect [NAME] [flags]
```

### Examples

```

  # Describe all the volumes:
  pxc volume inspect

  # Describe specific volume called "abc":
  pxc volume inspect abc

  # Describe list of volumes (abc, xyz)
  pxc volume inspect abc xyz
```

### Options

```
  -h, --help                 help for inspect
      --owner string         Owner of volume
      --show-k8s-info        Show kubernetes information
      --volumegroup string   Volume group id
```

### Options inherited from parent commands

```
      --pxc.config string       Config file (default is $HOME/.pxc/config.yml)
      --pxc.config-dir string   Config directory (default "/home/lpabon/.pxc")
      --pxc.context string      Force context name for the command
      --pxc.token string        Portworx authentication token
      --pxc.v int32             [0-3] Log level verbosity
```

### SEE ALSO

* [pxc volume](pxc_volume.md)	 - Volume life cycle management

###### Auto generated by spf13/cobra on 5-Mar-2020