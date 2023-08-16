# remote-build-tool
This repository contains a basic REST API application that provides an endpoint to trigger script execution on the server. It is intended to allow on-demand running of scripts via simple HTTP requests.


Uses conda environment. Create env with:

```
conda env create -f devenv.yml
```

Activate new environment:

```
conda activate remote-build-tool-env
```

Run the app:

```
python remote-build-tool-app.py
```

Alternatively, run in the background with:

```
nohup python remote-build-tool-app.py &
```

