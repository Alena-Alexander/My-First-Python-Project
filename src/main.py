from __config__ import getLogger

log = getLogger(__name__)


# 1
pangram = "The five boxing wizards jump quickly."
log.debug(pangram)

# string_object_or_list[start_index:end_index]
pangram[29:37]

if __name__ == "__main__":
    pass
