#!/usr/bin/env python3
"""
Rename obfuscated Java identifiers in com/threerings decompiled source.
"""

import re
from pathlib import Path

ROOT = Path("")

CLASS_RENAMES: dict[tuple[str, str], str] = {
    ("com.threerings", "a"): "ClydeLog",
    ("com.threerings", "b"): "Log",
    ("com.threerings", "c"): "NaryaLog",
    ("com.threerings", "d"): "NenyaLog",

    ("com.threerings.a", "a"): "GeomUtil",
    ("com.threerings.a", "b"): "Log",

    ("com.threerings.b", "a"): "RawImageReader",
    ("com.threerings.b", "b"): "ResourceUrlStreamHandler",
    ("com.threerings.b", "c"): "ResourceUrlConnection",
    ("com.threerings.b", "d"): "Log",
    ("com.threerings.b", "e"): "AbstractBundle",
    ("com.threerings.b", "f"): "ResourceManager",
    ("com.threerings.b", "g"): "RegisterUrlHandlerAction",
    ("com.threerings.b", "h"): "LoadClasspathResourceAction",

    ("com.threerings.admin", "a"): "Log",
    ("com.threerings.admin.client", "a"): "AdminService",
    ("com.threerings.admin.client", "b"): "FieldNameComparator",

    ("com.threerings.billing", "a"): "Log",
    ("com.threerings.bureau.a", "a"): "BureauService",
    ("com.threerings.coin.a", "a"): "CoinUtil",
    ("com.threerings.crowd", "a"): "Log",
    ("com.threerings.crowd.a", "a"): "CrowdContext",

    ("com.threerings.config", "a"): "ArgumentMapEntrySet",
    ("com.threerings.config", "b"): "ConfigGroupFunction",
    ("com.threerings.config", "c"): "ConfigAddedOp",
    ("com.threerings.config", "d"): "ConfigRemovedOp",
    ("com.threerings.config", "e"): "ConfigGroupListener",
    ("com.threerings.config", "f"): "ConfigGroupOrdering",
    ("com.threerings.config", "g"): "ConfigUpdatedOp",
    ("com.threerings.config", "h"): "ManagedConfigOrdering",
    ("com.threerings.config", "i"): "ConfigUpdateListener",
    ("com.threerings.config", "j"): "ManagedConfigUpdatedOp",
    ("com.threerings.config", "k"): "Shallow",
    ("com.threerings.config", "l"): "NullProperty",
    ("com.threerings.config", "m"): "ChoiceConfigSetter",
    ("com.threerings.config", "n"): "ChoiceProperty",
    ("com.threerings.config", "o"): "ConfigRef",
    ("com.threerings.config", "p"): "ConfigRefs",

    ("com.threerings.config.dist.a", "a"): "DConfigDirector",
    ("com.threerings.config.dist.a", "b"): "FlushTimer",
    ("com.threerings.config.dist.a", "c"): "RemoteFilteredListener",
    ("com.threerings.config.dist.a", "d"): "DConfigService",
    ("com.threerings.config.dist.b", "a"): "DConfigListener",

    ("com.threerings.config.util", "a"): "ConfigId",
    ("com.threerings.config.util", "b"): "NonSyntheticFieldPredicate",
    ("com.threerings.config.util", "c"): "FieldLister",
    ("com.threerings.config.util", "d"): "PublicNonTransientFieldPredicate",
    ("com.threerings.config.util", "e"): "FieldListCacheLoader",
    ("com.threerings.config.util", "f"): "FieldNameFunction",
    ("com.threerings.config.util", "g"): "DependencyContext",

    ("com.threerings.config.swing", "a"): "ClassToGroupNameFunction",
    ("com.threerings.config.swing", "b"): "ConfigFileFilter",
    ("com.threerings.config.swing", "c"): "TreeChooserOkListener",
    ("com.threerings.config.swing", "d"): "TreeChooserDoubleClickListener",
    ("com.threerings.config.swing", "e"): "SelectionEnableOkListener",
    ("com.threerings.config.swing", "f"): "ConfigTreeSelectionListener",
    ("com.threerings.config.swing", "g"): "ConfigTreeExpansionListener",
    ("com.threerings.config.swing", "h"): "SlashCountFunction",
    ("com.threerings.config.swing", "i"): "FilterTextChangeHandler",
    ("com.threerings.config.swing", "j"): "ConfigNameFilter",
    ("com.threerings.config.swing", "k"): "RecentConfigNotifyOp",

    ("com.threerings.config.tools", "a"): "UndoEditListener",
    ("com.threerings.config.tools", "b"): "EditMenuListener",
    ("com.threerings.config.tools", "c"): "MenuRefreshRunnable",
    ("com.threerings.config.tools", "d"): "XmlFileFilter",
    ("com.threerings.config.tools", "e"): "TabSelectionListener",
    ("com.threerings.config.tools", "f"): "ConfigRefNamePredicate",
    ("com.threerings.config.tools", "g"): "GroupPrefsListener",
    ("com.threerings.config.tools", "h"): "ConfigGroupChangeListener",
    ("com.threerings.config.tools", "i"): "EditorsRefreshOp",
    ("com.threerings.config.tools", "j"): "ManagerPanelComparator",
    ("com.threerings.config.tools", "k"): "ConfigGroupListenerImpl",
    ("com.threerings.config.tools", "l"): "ConfigSearchRunnable",
    ("com.threerings.config.tools", "m"): "SearchResultClickListener",
    ("com.threerings.config.tools", "n"): "ConfigSearchIterator",
    ("com.threerings.config.tools", "o"): "ConfigSearchResult",
    ("com.threerings.config.tools", "p"): "FileChildrenFunction",
    ("com.threerings.config.tools", "q"): "FileToSearchResultFunction",
    ("com.threerings.config.tools", "r"): "DirectoryChildrenFunction",
    ("com.threerings.config.tools", "s"): "NonSvnDirFilter",
    ("com.threerings.config.tools", "t"): "DatFileFilter",
    ("com.threerings.config.tools", "u"): "ConfigPresenceFinder",
    ("com.threerings.config.tools", "v"): "CompositeExporterAdapter",
    ("com.threerings.config.tools", "w"): "AddConfigTypeListener",
    ("com.threerings.config.tools", "x"): "ResourceDatFileFilter",
    ("com.threerings.config.tools", "y"): "ResourceXmlFileFilter",

    ("com.threerings.stats", "a"): "Log",
    ("com.threerings.media", "f"): "Log",
    ("com.threerings.miso", "a"): "Log",
    ("com.threerings.puzzle", "a"): "Log",
    ("com.threerings.openal", "i"): "Log",
    ("com.threerings.whirled", "a"): "Log",
    ("com.threerings.whirled.zone", "a"): "Log",
    ("com.threerings.presents", "a"): "Log",
    ("com.threerings.projectx", "a"): "Log",
    ("com.threerings.projectx.pvp", "a"): "Log",
    ("com.threerings.projectx.admin", "a"): "Log",
    ("com.threerings.projectx.design", "a"): "Log",
    ("com.threerings.projectx.craft", "a"): "Log",
    ("com.threerings.projectx.mission", "a"): "Log",
    ("com.threerings.projectx.exchange", "a"): "Log",
    ("com.threerings.projectx.guild", "a"): "Log",
    ("com.threerings.projectx.item", "a"): "Log",
    ("com.threerings.projectx.trade", "a"): "Log",
    ("com.threerings.projectx.dungeon.arena", "a"): "Log",
    ("com.threerings.projectx.dungeon", "a"): "Log",
}

FIELD_RENAMES: dict[str, dict[str, str]] = {
    "com/threerings/b/a.java": {"bPh": "colorMapCache", "agE": "zeroOrigin"},
    "com/threerings/b/b.java": {"bPi": "resourceManager"},
    "com/threerings/b/c.java": {"bPj": "inputStream", "bPk": "handler"},
    "com/threerings/b/f.java": {
        "aeQ": "classLoader", "bPl": "resourceDir",
        "bPm": "resourcePrefix", "bPn": "altPrefix",
        "bPo": "unpackEnabled", "bPp": "bundles",
        "bPq": "setBundles", "bPr": "pathMapper",
        "bPs": "watchedFiles", "bPt": "notifyOp",
        "bPx": "observers", "acb": "resourcePath",
    },
    "com/threerings/b/g.java": {"bPu": "resourceManager"},
    "com/threerings/b/h.java": {"bPv": "resourcePath", "bPw": "resourceManager"},
    "com/threerings/config/util/a.java": {"NX": "configClass", "NY": "configName"},
    "com/threerings/config/util/b.java": {"Oa": "gatherer"},
    "com/threerings/config/util/c.java": {"Oe": "fieldPredicate", "Of": "fieldCache"},
    "com/threerings/config/util/e.java": {"Og": "fieldLister"},
    "com/threerings/config/util/f.java": {"Oh": "cacheLoader"},
    "com/threerings/config/a.java": {"LM": "argumentMap", "LK": "entries"},
    "com/threerings/config/b.java": {"LN": "configGroup"},
    "com/threerings/config/c.java": {"LO": "configEvent", "LP": "group"},
    "com/threerings/config/d.java": {"LQ": "configEvent", "LR": "group"},
    "com/threerings/config/f.java": {"LS": "configManager"},
    "com/threerings/config/g.java": {"LT": "configEvent", "LU": "configManager"},
    "com/threerings/config/h.java": {"LV": "configManager"},
    "com/threerings/config/j.java": {"Ma": "configEvent", "Mb": "config"},
    "com/threerings/config/m.java": {"Mi": "choiceParam"},
    "com/threerings/config/n.java": {"Mj": "wrappedProperty", "Mk": "choiceParam"},
    "com/threerings/config/dist/a/a.java": {
        "Mm": "configObject", "Mn": "removedKeys",
        "Mo": "lastFlushTime", "Mp": "flushTimer",
    },
    "com/threerings/config/dist/a/b.java": {"Mq": "director"},
    "com/threerings/config/dist/a/c.java": {"Mr": "director"},
    "com/threerings/admin/client/b.java": {"LD": "fieldNames", "LE": "editorPanel"},
    "com/threerings/config/swing/b.java": {
        "Mt": "messageManager", "Mu": "configType", "Mv": "chooser"},
    "com/threerings/config/swing/c.java": {
        "Mw": "configTree", "Mx": "confirmed", "My": "dialog", "Mz": "chooser"},
    "com/threerings/config/swing/d.java": {
        "MA": "configTree", "MB": "confirmed", "MC": "dialog", "MD": "chooser"},
    "com/threerings/config/swing/e.java": {"ME": "configTree", "MF": "chooser"},
    "com/threerings/config/swing/f.java": {"MI": "configTree"},
    "com/threerings/config/swing/g.java": {"MJ": "configTree"},
    "com/threerings/config/swing/h.java": {"MK": "configTree"},
    "com/threerings/config/swing/i.java": {"MN": "filterPanel"},
    "com/threerings/config/swing/j.java": {"MO": "filterText", "MP": "handler"},
    "com/threerings/config/swing/k.java": {"MR": "configRef", "MS": "recentList"},
    "com/threerings/config/tools/a.java": {"MU": "editor"},
    "com/threerings/config/tools/b.java": {"MV": "menu", "MW": "itemIndex", "MX": "editor"},
    "com/threerings/config/tools/c.java": {"MY": "menuListener"},
    "com/threerings/config/tools/d.java": {"MZ": "editor"},
    "com/threerings/config/tools/e.java": {"Na": "editor"},
    "com/threerings/config/tools/f.java": {"Nb": "exactMatch", "Nc": "name", "Nd": "editor"},
    "com/threerings/config/tools/g.java": {"Ne": "prefKey", "Nf": "combo", "Ng": "editor"},
    "com/threerings/config/tools/h.java": {"Nh": "editor"},
    "com/threerings/config/tools/j.java": {"Nl": "managerPanel"},
    "com/threerings/config/tools/k.java": {"Np": "configPanel", "Nm": "configGroup"},
    "com/threerings/config/tools/l.java": {
        "Nr": "resultIterator", "Ns": "groupIterator",
        "Nt": "searchFunc", "Nu": "groupIterable", "Nv": "searcher"},
    "com/threerings/config/tools/m.java": {"Nw": "searchEntry", "Nx": "searcher"},
    "com/threerings/config/tools/n.java": {
        "Ny": "configIterator", "Nz": "groupIterator",
        "NA": "currentGroup", "NB": "searchSource", "NC": "searcherContext"},
    "com/threerings/config/tools/o.java": {
        "ND": "configGroup", "NE": "config", "NF": "iterator"},
    "com/threerings/config/tools/p.java": {"NK": "fileSearcher"},
    "com/threerings/config/tools/q.java": {"NL": "searchFunc", "NM": "fileSearcher"},
    "com/threerings/config/tools/r.java": {"NN": "fileFilter", "NO": "fileSearcher"},
    "com/threerings/config/tools/u.java": {"NQ": "configClass", "NR": "refPredicate"},
    "com/threerings/config/tools/v.java": {"NS": "adapters"},
    "com/threerings/config/tools/w.java": {"NT": "configType", "NU": "editor"},
    "com/threerings/config/tools/x.java": {"NV": "editor"},
    "com/threerings/config/tools/y.java": {"NW": "editor"},
}

# ─────────────────────────────────────────────────────────────
# Auto-detect logger-only classes
# ─────────────────────────────────────────────────────────────

LOGGER_RE = re.compile(
    r'^(package\s+[\w.]+\s*;\s*)?(import\s+[\w.]+\s*;\s*)*'
    r'public\s+class\s+\w+\s*\{\s*'
    r'public\s+static\s+Y\s+GM\s*=\s*Y\.ax\([^)]+\)\s*;\s*\}\s*$',
    re.DOTALL
)

def pkg_of(text):
    m = re.search(r'^package\s+([\w.]+)\s*;', text, re.MULTILINE)
    return m.group(1) if m else ""

def cls_of(text):
    m = re.search(r'\b(?:class|interface|enum|@interface)\s+([A-Za-z_]\w*)', text)
    return m.group(1) if m else ""

java_files = sorted(ROOT.rglob("*.java"))
for path in java_files:
    text = path.read_text(errors="replace")
    p, c = pkg_of(text), cls_of(text)
    if p and c and (p, c) not in CLASS_RENAMES and len(c) == 1 and c.islower():
        if LOGGER_RE.match(text.strip()):
            CLASS_RENAMES[(p, c)] = "Log"

print(f"Class renames planned: {len(CLASS_RENAMES)}")

# ─────────────────────────────────────────────────────────────
# Build a map: declaring file path → (old_cls, new_cls)
# ─────────────────────────────────────────────────────────────
declaring: dict[Path, tuple[str, str]] = {}
for (pkg, old_cls), new_cls in CLASS_RENAMES.items():
    if old_cls == new_cls:
        continue
    fpath = ROOT / pkg.replace(".", "/") / f"{old_cls}.java"
    if fpath.exists():
        declaring[fpath] = (old_cls, new_cls)

# ─────────────────────────────────────────────────────────────
# APPLY RENAMES TO FILE CONTENT
# ─────────────────────────────────────────────────────────────

changed = 0
for path in java_files:
    text = path.read_text(errors="replace")
    orig = text
    rel = str(path.relative_to(ROOT))

    # A. CLASS RENAMES
    for (pkg, old_cls), new_cls in CLASS_RENAMES.items():
        if old_cls == new_cls:
            continue

        # A1. Import line: exact match, always safe
        old_import = f"import {pkg}.{old_cls};"
        new_import = f"import {pkg}.{new_cls};"
        if old_import in text:
            text = text.replace(old_import, new_import)

        # A2. Fully-qualified reference: pkg.OldCls NOT followed by an identifier char
        #     This avoids  com.foo.a  matching inside  com.foo.admin
        fq_old = re.escape(f"{pkg}.{old_cls}")
        fq_new = f"{pkg}.{new_cls}"
        text = re.sub(fq_old + r'(?![A-Za-z0-9_])', fq_new, text)

        # A3. Declaring file: rename the class declaration header
        if path in declaring and declaring[path] == (old_cls, new_cls):
            # Rename class/interface/enum/annotation declaration only
            text = re.sub(
                r'\b(class|interface|enum|@interface)\s+' + re.escape(old_cls) + r'\b',
                r'\1 ' + new_cls,
                text
            )

    # B. FIELD RENAMES (file-scoped)
    if rel in FIELD_RENAMES:
        for old_f, new_f in FIELD_RENAMES[rel].items():
            text = re.sub(r'(?<![A-Za-z0-9_])' + re.escape(old_f) + r'(?![A-Za-z0-9_])',
                          new_f, text)

    # C. GM → log  (logger field)
    #    Only: "Y GM" in declarations, and ".GM" in accesses
    text = re.sub(r'\bY\s+GM\b', 'Y log', text)
    text = re.sub(r'(?<=\.)GM\b', 'log', text)

    if text != orig:
        path.write_text(text)
        changed += 1

print(f"Files content-modified: {changed}")

# ─────────────────────────────────────────────────────────────
# RENAME .java FILES
# ─────────────────────────────────────────────────────────────
renamed = 0
for old_path, (old_cls, new_cls) in declaring.items():
    new_path = old_path.with_name(f"{new_cls}.java")
    if old_path.exists() and not new_path.exists():
        old_path.rename(new_path)
        print(f"  {old_path.relative_to(ROOT)}  →  {new_cls}.java")
        renamed += 1

print(f"\nFiles renamed: {renamed}")
print("Done.")
