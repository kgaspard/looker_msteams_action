action: {
  label: "Send this to Microsoft Teams"
  url: "[YOUR_CLOUD_FUNCTION_TRIGGER]"

  param: {
    name: "msteamswebhook"
    value: "[YOUR_MS_TEAMS_WEBHOOK]"
  }

  param: {
    name: "link"
    value: "[LINK_TO_THE_DASHBOARD]"
  }

  param: {
    name: "linktext"
    value: "[YOUR_LINK_TEXT_IN_THE_CARD]"
  }

  form_param: {
    name: "Title"
    type: string
    default: "Check this out"
  }

  form_param: {
    name: "Message"
    type: textarea
    default: "Hey,
Could you check out the latest on {{value}}?"
  }
}