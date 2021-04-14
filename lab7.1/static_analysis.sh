#! /usr/bin/env bash

REPO="https://github.com/DnPlas/adc-softwaresystems.git"
REPO_SUFFIX="dnplas-adc-softwaresystems"
CLONE="sa_$REPO_SUFFIX"
current_time=$(date "+%Y.%m.%d-%H.%M.%S")

function check_install(){
    if ! command prospector &> /dev/null;
    then
	    echo "prospector is not installed, exiting"
	    exit
    fi

    if ! command radon &> /dev/null;
    then
	    echo "radon is not installed, exiting"
	    exit
    fi

#    if ! command git &> /dev/null;
#    then
#	    echo "git is not installed, exiting"
#	    exit
#    fi
#
}

function clone_repo(){
    git clone $REPO $CLONE
    cd $CLONE && \
    mkdir sa_logs

}

function run_sa(){
    prospector > sa_logs/sa_prospector_$current_time.out
    radon cc . > sa_logs/cc_radon_$current_time.out
    radon raw . > sa_logs/raw_radon_$current_time.out
    radon mi . > sa_logs/mi_radon_$current_time.out
    radon hal . > sa_logs/hal_radon_$current_time.out
}

function main(){
	check_install
	clone_repo
	run_sa
}

echo "Running Static Analysis for all .py files in this directory and child directories"
echo "Reports can be found in sa_logs/"
main
